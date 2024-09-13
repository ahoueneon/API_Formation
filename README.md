J'ai à la base pris ce projet sur ce repos https://github.com/OpenClassrooms-Student-Center/7192416_APIs_DRF,
que je veux maintenant modifier en lui ajoutant une API afin de pouvoir la faire communiquer avec d'autre systeme et avoir acces aux données. 

Mon objectif ici est de pouvoir creer une API pour pouvoir et non creer une application. Raison pour laquelle je part sur un projet existant. 

# CE QUE j'AI AJOUTE

# 1- Créez un premier endpoint

En avant, mettons en place ce premier endpoint en permettant à nos visiteurs d’accéder à la liste des catégories de nos produits.
DRF met à notre disposition des serializers qui permettent de transformer nos models Django en un autre format qui, lui, est exploitable par une API.
Lorsque notre API sera consultée, le serializer va nous permettre de transformer notre objet en un JSON et, inversement, lorsque notre API va recevoir du JSON, elle sera capable de le transformer en un objet

Créons un fichier  serializers.py  et écrivons notre premier serializer, que nous nommerons  CategorySerializer  pour rester clair et précis. ;)

Il est nécessaire de définir sa classe  Meta  et la liste des champs, exactement comme pour un formulaire. De plus, les noms des attributs sont identiques.

On cree differents endpoint pour avoir la liste des Articles, des produits et des catégories.

