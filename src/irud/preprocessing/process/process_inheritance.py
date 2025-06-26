

inheritance = {
    "AR" : "GENO:0000148",
    "AD" : "GENO:0000147",
    "XLD" : "GENO:0000146",
    "XLR" : "GENO:0000149",
}

def process_inheritance():
    """
    This function filters out all the different inheritance strings from the CSV file and maps them to the GENO ontology.
    E.G. :
        "AD" -> "GENO:0000147"
        "ADde novo" -> "GENO:0000147"
        "de novoAD" -> "GENO:0000147"
        "AR" -> "GENO:0000148"
        "AR" -> "GENO:0000148"
        
    output: 
        - processed data into a column
    """
    
    # filter and search for AD/AR/XLD/XLR in the inheritance column
    
    # use mapping to process
    
    
    pass    