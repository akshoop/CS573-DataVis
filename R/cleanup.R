# R script file for CS 573 Data Vis
# file cleanup
library(ggplot2)
setwd("/Users/SHOOP/Google Drive/CS 573 Data Viz/github-projs/DataVisFinal/CSV/")
file = read.csv('liquor-licenses-orig.csv',sep = ',',header = TRUE)
head(file)
# check for na
colnames(file)[colSums(is.na(file)) > 0]

