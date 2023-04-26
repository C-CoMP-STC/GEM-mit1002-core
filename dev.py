# A function that checks if a specific reaction is a maintenace reaction
# by checking if the reaction has only ATP and water as reactants and
# only ADP, hydrogen, and phosphate as products.
def is_maintenance_reaction(model, reaction):
    # A list of the IDs of the reactants and products that are allowed
    # in a maintenance reaction. Have to specify the compartment of the
    # metabolites, this may be a problem if different models use
    # different compartment IDs.
    # ATP and water are allowed reactants.
    allowed_reactants = ['cpd00002_c0', 'cpd00001_c0']
    # ADP, phosphate, and protons are allowed products.
    allowed_products = ['cpd00008_c0', 'cpd00009_c0', 'cpd00067_c0']
    # Check if the reaction has only the allowed reactants and products
    # in any order.
    if any (met.id not in allowed_reactants for met in reaction.reactants):
        return False
    if any (met.id not in allowed_products for met in reaction.products):
        return False
    else:
        return True

# A function that searches all the reactions in a model for a maintenance
# reaction, and returns the reaction if it finds one.
def find_maintenance_reaction(model):
    maintenace_rxns = []
    for reaction in model.reactions:
        if is_maintenance_reaction(model, reaction):
            maintenace_rxns.append(reaction)
    # If there is only one maintenance reaction, return it.
    if len(maintenace_rxns) == 1:
        return maintenace_rxns[0]
    # If there are no maintenance reactions, return None.
    elif len(maintenace_rxns) == 0:
        return None
    # If there are multiple maintenance reactions, return a list of them
    # and print a warning.
    else:
        print('Warning: multiple maintenance reactions found.')
        return maintenace_rxns