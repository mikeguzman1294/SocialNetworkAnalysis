You are a data scientist at LinkedIn. Your colleagues from Marketing want to organize an online marketing campaign for their client, a restaurant in the Bay area (San Francisco Bay area, not Brest Bay area, by the way). They have read a lot about social network analysis and ask you to find the 5 most influential people on the network who would be best to promote the restaurant.

You are a smart data scientist, and you know that influence is not enough. You have to find the users who are influencers but also located in the right area! As you know your dataset perfectly, you are aware that only 40% of the users have provided their location in their profile... But as you know about homophily: nodes that are connected to each other in a social network tend to be similar in their features. This property is
captured by a popular proverb: “birds of a feather flock together.” So you have a plan:  prepare your dataset to fill uncomplete profiles, you will use their neighbors' attributes!

Of course, a data scientists bring proofs, justify their results. Compare your strategy to fill the profile with the "ground truth" (i.e. real data, given in the coding material), and compare also different strategies to select the best one! We provide you with a baseline (known) method in order to compare your proposal with its (lower, of course lower) results. To measure the relevance of your profile filling strategy, you can use accuracy.

What could you do to test your detection of influencers? This step is called the evaluation of your model (cf. CRISP-DM steps). It is a very important step to decide whether you will deploy your method.... or if it will just remain a lab toy!

Your challenge is to find influencers able to promote a restaurant in the Bay Area