

child1 = ['1', '7', '5', '4', '8', '2', '6', '9']
child2 = ['8', '9', '1', '2', '5', '4', '3', '6']
k = 4

print("Parent 1: ", child1)
print("Parent 2: ", child2)

root_gene1 = child1[:k]
root_gene2 = child2[:k]

print("Root gene 1: ", root_gene1)
print("Root gene 2: ", root_gene2)

rear_gene1 = child1[k:]
rear_gene2 = child2[k:]

print("Rear gene 1: ", rear_gene1)
print("Rear gene 2: ", rear_gene2)

# if root_gene1 elements are same in rear_gene2, remove those elements
for gene in root_gene1:
    if gene in rear_gene2:
        rear_gene2.remove(gene)

print("After Removing Same Elements Rear gene 2: ", rear_gene2)

# if root_gene2 elements are same in rear_gene1, remove those elements
for gene in root_gene2:
    if gene in rear_gene1:
        rear_gene1.remove(gene)

print("After Removing Same Elements Rear gene 1: ", rear_gene1)

# if root_gene2 elements are not in rear_gene2, add those elements
for gene in root_gene2:
    if gene not in rear_gene2 + root_gene1:
        rear_gene2.append(gene)
    if len(root_gene1) + len(rear_gene2) == 8:
        break
    

print("After Adding Missing Elements Rear gene 2: ", rear_gene2)

# if root_gene1 elements are not in rear_gene1, add those elements
for gene in root_gene1:
    if gene not in rear_gene1 + root_gene2:
        rear_gene1.append(gene)
    if len(root_gene2) + len(rear_gene1) == 8:
        break

print("After Adding Missing Elements Rear gene 1: ", rear_gene1)

# combine root_gene1 and rear_gene2
child1 = root_gene1 + rear_gene2
child2 = root_gene2 + rear_gene1

# print
print("Child 1: ", child1)
print("Child 2: ", child2)


