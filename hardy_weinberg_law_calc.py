# This program will calculate the fraction of individuals with the recessive 
# phenotype, the fraction of the recessive allele, and the fraction with
# heterozygous genotype
import math

# User inputs the number of individuals with dominant and recessive phenotypes
dominant = input("Enter the number of individuals with the dominant phenotype: ")
recessive = input("Enter the number of individuals with the recessive phenotype: ")

# Change the variables into integers
dominant = int(dominant)
recessive = int(recessive)

# Calculate the total population to get the frequency of those with the recessive phenotype
totalPop = dominant + recessive

# Calculate the frequency of the recessive phenotype and allele
q2 = recessive / totalPop
q = math.sqrt(q2)

# Calculate the frequency of the dominant alleles
p = 1 - q

# Calculate frequency of each of each genotype
RR = p**2
Rr = 2 * p * q
rr = q**2

# Print answers
print("Fraction of recessive phenotype: ", rr)
print("Fraction of recessive allele: ", q)
print("Fraction of heterozygous genotype: ", Rr)