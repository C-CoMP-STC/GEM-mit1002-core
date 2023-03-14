import cobra

# Load the E. coli core model
ecoli = cobra.io.load_model('textbook')

# Get a list of all the metabolites using the BiGG IDs
ecoli_mets = [met.annotation['bigg.metabolite'] for met in ecoli.metabolites]

# Load the Alteromonas model
alt = cobra.io.read_sbml_model('core_314275.5_GP.SBML/core_314275.5_GP.xml')

# Print some basic info

# Make lists to hold metabolites
# common_mets = []
# alt_only_mets = []
# alt_mets_w_no_bigg_id = []
# ecoli_only_mets = [] # FIXME: Not actully using this

# # Loop through the Alteromonas model's metabolites
# for met in alt.metabolites:
#     # Check if the metabolite has a BiGG ID, if not skip it
#     if 'bigg.metabolite' not in met.annotation.keys():
#         alt_mets_w_no_bigg_id.append(met)
#         continue
#     # Get the bigg metabolite id
#     bigg_met = met.annotation['bigg.metabolite']
#     # Check if the metabolite is in the E. coli model
#     if bigg_met in ecoli_mets:
#         common_mets.append(met)
#     else:
#         alt_only_mets.append(met)

# Make lists to hold reactions
common_rxns = []
alt_only_rxns = []
alt_rxns_w_no_bigg_id = []
ecoli_only_rxns = []
ecoli_rxns_with_no_bigg_id = []
ecoli_rxns_with_no_metanetx_id = []

# Print the bigg reaction IDs for the reactions in the E. coli model
# to a file, one ID per line
# Only need to do once
# with open('ecoli_rxns.txt', 'w') as f:
#     for rxn in ecoli.reactions:
#         f.write(rxn.annotation['bigg.reaction'] +'\n')
# Generate id-mapper using https://www.metanetx.org/cgi-bin/mnxweb/id-mapper

# Read in the id-mapper tsv file as a dictionary
id_mapper = {}
with open('id-mapper.tsv', 'r') as f:
    for line in f:
        line = line.strip().split('\t')
        if len(line) > 1:
            id_mapper[line[0]] = line[1]
        else:
            id_mapper[line[0]] = None

# Get list of metanetx reaction IDs for the alt model
alt_reactions = [rxn.annotation['metanetx.reaction'] for rxn in alt.reactions if 'metanetx.reaction' in rxn.annotation.keys()]

# Loop through the Alteromonas model's reactions
for rxn in ecoli.reactions:
    if 'bigg.reaction' not in rxn.annotation.keys():
        ecoli_rxns_with_no_bigg_id.append(rxn)
        continue
    bigg_rxn = rxn.annotation['bigg.reaction']
    if bigg_rxn in id_mapper.keys():
        metanetx_rxn = id_mapper[bigg_rxn]
        if metanetx_rxn is None:
            ecoli_rxns_with_no_metanetx_id.append(rxn)
        elif metanetx_rxn in alt_reactions:
            common_rxns.append(rxn)
        else:
            ecoli_only_rxns.append(rxn)



print(ecoli)

