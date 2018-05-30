#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 30 00:11:27 2018

@author: ywan
"""

import pysam as py
import numpy as np

# Input BAM and BED
path_bam = '/home/ywan/localdata/test1/BioEng_Bioinformatics/Test_AH/TEST1.bam'
path_bed = '/home/ywan/localdata/test1/BioEng_Bioinformatics/Test_AH/TEST1_region.bed'
  
def Bam_prepare(path_bam):
    samraw = py.AlignmentFile(path_bam, 'rb')
    # Sort and index
    try:
        samraw.check_index()
    except ValueError:
        py.sort('-o', '/home/ywan/localdata/test1/BioEng_Bioinformatics/Test_AH/sorted.bam', path_bam)
        py.index('/home/ywan/localdata/test1/BioEng_Bioinformatics/Test_AH/sorted.bam')
        path_bam = '/home/ywan/localdata/test1/BioEng_Bioinformatics/Test_AH/sorted.bam'
        return(py.AlignmentFile(path_bam, 'rb'), path_bam)
        #print('Is there index: %s'%(samraw.check_index())) ## Check index    
samraw, path_bam = Bam_prepare(path_bam)

# =============================================================================
# Q1. Average sequencing quality
# =============================================================================

def Average_quality(sam_class):
    seqq = []
    for line in sam_class:
        temp = np.array(line.query_qualities)
        seqq.append(temp.mean())
    
    seqq = np.array(seqq)                                       ## Seq quality of each read
    seqq_ave = seqq.mean()                                      ## Average sequencing quality
    print('Average sequencing quality: {0:.2f}'.format(seqq_ave))  
    del seqq 
    
Average_quality(samraw)

# =============================================================================
# Q2. Percentage of reads enriched in the target regions 
# =============================================================================

import pybedtools as bd


def Bed_prepare(path_bed, path_bam):
    # prepare bed_class
    target = bd.BedTool(path_bed)
    bam = bd.BedTool(path_bam)
    temp = bam.bam_to_bed(stream=True).saveas()                   ## temp bam file as bed_class
    target = target.remove_invalid().saveas()
    return(bam, temp, target)

def Read_enrichment(target, temp):
    ontag_reads = temp.coverage(target, counts=True).sort()        ## Reads mapped on target regions
    read_count = np.array([int(line[-1]) for line in ontag_reads]) 
                  
    Per_ontag = read_count.sum()/samraw.mapped*100                 ## Percentage of reads enriched in the target regions
    
    print('Percentage of reads enriched in the target regions: {0:.2f}%'.format(Per_ontag))    

bam, temp, target = Bed_prepare(path_bed, path_bam)
Read_enrichment(target, temp)

# =============================================================================
# Q3. Percentage of bases enriched in the target regions
# =============================================================================

import pandas as pan


def Base_enrichment(temp,bam, target):
    tagcov_base = target.coverage(temp, d=True)
    
    ontag_base = np.array([int(base[5]) for base in tagcov_base])  ## the depth at each position on target
    genomecov_base = bd.BedTool.genome_coverage(bam, dz=True)      ## the depth at each position on genome    
    gencov_perbase = pan.read_table(genomecov_base.fn, names=['chrom', 'position', 'depth'])
    gencov_allbase = (gencov_perbase.iloc[:, 2]).sum()             ## Total bases mapped on genome
    
    
    Per_base = ontag_base.sum()/gencov_allbase*100
    print('Percentage of bases enriched in the target regions: {0:.2f}%'.format(Per_base))
    return(ontag_base, tagcov_base)

ontag_base, tagcov_base = Base_enrichment(temp,bam,target)

# =============================================================================
# Q4. Uniformity of coverage 
# =============================================================================

def Uniformity_cov(ontag_base):
    total_tag_base = np.array([region.length for region in target])
    Mean_cov = ontag_base.sum()/total_tag_base.sum()              ## Mean coverage of target regions
    condition = 0.2*Mean_cov             
    lager_02mean = np.where(ontag_base > condition, 1, 0)
    uc = lager_02mean.sum()/lager_02mean.shape[0]*100             ## Uniformiity of coverage
    
    print('Uniformity of coverage: {0:.2f}%'.format(uc))
    return(Mean_cov, total_tag_base)

Mean_cov, total_tag_base = Uniformity_cov(ontag_base)

# =============================================================================
# Q5. Mean coverage for each base in all target regions
# =============================================================================

print('Mean coverage for each base in all target regions: {0:.2f}'.format(Mean_cov))

# =============================================================================
# Q6. An output tab-delimited txt file
# =============================================================================

def Output(path_bed, path_bam, tagcov_base, total_tag_base):
    region_base = py.bedcov(path_bed, path_bam).split('\n')      ## Total base depth per tag-region
    region_base.pop(-1)    
    region_base = pan.DataFrame([line.split('\t') for line in region_base], columns = ['Chromosome', 'Start', 'Stop', 'RegionID', 'MeanCoverage'])
    region_base.iloc[:, 4] = region_base.iloc[:, 4].map(lambda x: int(x))/total_tag_base
    region_base = region_base.reset_index()
    region_base = region_base.set_index('RegionID')
    
    # depth of each positon in target region
    region_perbase = pan.DataFrame([([line[i] for i in [3,5]]) for line in tagcov_base], columns =['RegionID', 'Depth']) ## base depth on target region
    region_perbase.iloc[:, 1] = region_perbase.iloc[:, 1].map(int) 
    # Compute Std
    StdCov = region_perbase.groupby(region_perbase['RegionID']).std() ## StdDev
    StdCov.columns = ['StdDevCoverage']
    # Merge two dataframe
    df_list = [region_base, StdCov] 
    output = pan.concat(df_list, axis = 1,ignore_index = False).sort_values('index')
    output = output.reset_index()
    reg_col = output.pop('level_0')
    output.insert(4, 'RegionID', reg_col)
    del output['index']
    
    output.to_csv('output.txt', index= None, sep='\t', float_format = '%.2f')

Output(path_bed, path_bam, tagcov_base, total_tag_base)
