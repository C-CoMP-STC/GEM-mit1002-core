# A function that checks if a specific reaction is a maintenace reaction
# by checking if the reaction has one reactant and one product, and
# those are ATP and ADP, respectively.
def is_maintenance_reaction(model, reaction):
    if len(reaction.reactants) == 1 and len(reaction.products) == 1:
        if reaction.reactants[0].id == 'cpd00002' and reaction.products[0].id == 'cpd00008':
            return True
    return False

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