#!/usr/bin/env python
# coding: utf-8

# Pet Shop Entity-Relationship Diagram
# 
# Group 14
# 
# Ragni Mehta
# 
# Eric Shumway
# 
# Luis Munoz
# 
# Kunlong Li
# 
# Junwei Shang

# ![Screenshot%202019-10-04%2023.04.28.png](attachment:Screenshot%202019-10-04%2023.04.28.png)

# The diagram above is used to show the database within a local pet shop. The main entities are the following: The store itself, the pets, the fish, and the customers. The entities' relationships' with other things in the store are also shown above such as how many fish are stored in fresh water tanks vs salt water tanks, and the foods that are linked to the fishes/pets vs the food that is linked to the consumer purchases. This relationship will come in handy when trying to observe and/or create a budget on overall food purchases while still separating what will be used by the animals vs customers. The entities and relationships are as follows: The pet store table has three main attributes that we are currently focusing on. The pets, the fishes, and the customers. The pets have their own attributes such as what enclosures they are kept in, the price of the pets, the quantity of the pets in the pet shop, and the food that they all require. The pet store has a one to many relationship with their pets: There is one pet shop, many unique pets. At most, 10 pets would be shopped for at a time which is setting the limit in the 'many' side of the relationship. The pets have a one to one relationship with the enclosures that they are kept in. Each unique pet is kept in one unique enclosure. The same is relevant for the fish. The pet store also has a one to many relationship with the fishes. There is one store, several fish. The fish have several attributes as well, including an attribute showing if either the fish is kept in a salt water tank or a fresh water tank depending on the breed. This creates a (0,1) relationship between the fish and the fish tank. The unique fish can only be kept in either one or the other tank. The tank on the other end could either just have one fish or many resulting in a (1,N) relationship. The consumer could purchase up to 10 fish at a time creating the limit (1,10) between fishes sold at the store. There is a relationship between the consumer and the store which is labeled as 'buys'. The consumer and the store would have a one to many relationship. There is one store, one or many unique customer(/s). The customer attributes would be the following: their name, and their purchases. The attributes in their table such as pet purchases, fish purchases, and food purchases would have a (0,N) relationship with their respective tables for pets, fish, and food. The consumer could either buy 0 of these things or many. Customer loyalty would be an optional attribute as not all customers would have this attribute.

# In[ ]:




