current_wd <- getwd()
#method to merge two csv files, where samples are identified by the last four digits in one of them, and the other by "sample id"
merge_csv <- function(files_directory=current_wd){
  #loading the 2 csv from the given file directory, if no directory given, the working directory will be used
  id <- read.csv(file.path(files_directory, "id.csv"))
  ssn <- read.csv(file.path(files_directory, "ssn.csv"))
  #extracting last 4 ssn from sample id
  #first we split the sample ID according to the underscore
  split_id <- sapply(as.vector(id[,1]), function(sample) strsplit(sample, "_"))
  #taking the second element in each sample id, i.e. the four digits ssn strings, then convert them to numerical values and storing it in a vector
  last4 <- as.vector(sapply(split_id, function(ssn) as.numeric(ssn[2])))
  #converting the ssn vector into matrix and give it a colname matching the colname of ssn in the other csv, i.e. "Last.4"
  last4 <- as.matrix(last4)
  colnames(last4) <- list("Last.4")
  #binding by column the newly created column of ssn that we extracted from the sample id and adding it to the original csv
  id_ssn <- cbind(id, last4)
  #merging the two csv using the common id column, i.e. "Last.4" and then writing the result to a newly created csv named "merged.csv"
  merged <- merge(id_ssn, ssn, by.x = "Last.4")
  write.csv(merged, file="merged.csv")
}

#calling the merge method
merge_csv()

#loading the newly created merged csv data
merged <- read.csv(file.path(current_wd, "merged.csv"))













