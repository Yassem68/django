from django.shortcuts import render, HttpResponseRedirect
from .forms import ResauxForm, CreateurForm
from . import models

def accueil(request):
    tmplate = "accueil.html"
    return  render(request, 'appli/accueil.html')

def ajout(request):
    if request.method == "POST":
        form = ResauxForm(request)
        return render(request, "appli/ajout.html", {"form" : form})
    else:
        form = ResauxForm()
        return render(request, "appli/ajout.html", {"form" : form})


def ajoutc(request):
    if request.method == "POST":
        form = CreateurForm(request)
        return render(request, "appli/ajoutc.html", {"form" : form})
    else:
        form = CreateurForm()
        return render(request, "appli/ajoutc.html", {"form" : form})


def traitement(request):
    rform = ResauxForm(request.POST)
    if rform.is_valid():
        reseaux = rform.save()
        return HttpResponseRedirect ("/appli/affichage")
    else:
        return render(request,"appli/ajout.html", {"form" : rform})

def traitementc(request):
    cform = CreateurForm(request.POST)
    if cform.is_valid():
        createur = cform.save()
        return HttpResponseRedirect ("/appli/affichagec/")
    else:
        return render(request,"appli/ajoutc.html", {"form" : cform})



def affichage(request):
    liste = list(models.Reseaux.objects.all())
    return render(request, 'appli/affichage.html', {"liste" : liste})

def affichagec(request):
    listes = list(models.Createur.objects.all())
    return render(request, 'appli/affichagec.html', {"listes" : listes})

def affiche(request, id):
    reseaux = models.Reseaux.objects.get(pk = id)
    return render(request, 'appli/affiche.html',{"reseaux": reseaux})

def affichec(request, id):
    createur = models.Createur.objects.get(pk = id)
    return render(request, 'appli/affichec.html',{"createur": createur})

def update(request,id):
    reseaux = models.Reseaux.objects.get(pk = id)
    form = ResauxForm(reseaux.dico())
    return render(request, 'appli/ajout.html', {"form": form, "id": id})

def updatetraitement(request,id):
    rform = ResauxForm(request.POST)
    if rform.is_valid():
        reseaux = rform.save(commit = False)
        reseaux.id = reseaux
        reseaux.save()
        return HttpResponseRedirect('/appli/affichage/', {"form": rform, "id" : id})
    else:
        return render(request, "appli/ajout.html", {"form": rform, "id": id})

def updatec(request,id):
    createur = models.Createur.objects.get(pk = id)
    form = CreateurForm(createur.dico2())
    return render(request, 'appli/ajoutc.html', {"form": form, "id": id})

def updatetraitementc(request,id):
    cform = CreateurForm(request.POST)
    if cform.is_valid():
        reseaux = cform.save(commit = False)
        reseaux.id = reseaux
        reseaux.save()
        return HttpResponseRedirect('/appli/affichagec/', {"form": cform, "id" : id})
    else:
        return render(request, "appli/ajoutc.html", {"form": cform, "id": id})

def delete(request, id):
    reseaux = models.Reseaux.objects.get(pk = id)
    reseaux.delete()
    return HttpResponseRedirect ('/appli/affichage')

def deletec(request, id):
    createur = models.Createur.objects.get(pk = id)
    createur.delete()
    return HttpResponseRedirect('/appli/affichagec')