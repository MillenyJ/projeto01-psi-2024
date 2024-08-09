from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, "index.html")

def jogadores(request):
    jogadores_list = [
    {"nome": "Barbara", "idade": "36", 
     "posicao": "Goleiro", 
     "nascimento": "1", 
     "foto": "jogadora9.jpg"},
    
    {"nome": "Duda Sampaio.", "idade": "23", 
     "posicao": "Atacante", 
     "nascimento": "2", 
     "foto": "jogadora8.jpg"},
    
    {"nome": "Tamires", "idade": "37", 
     "posicao": "Defensor", 
     "nascimento": "3", 
     "foto": "jogadora7.jpg"},
    
    {"nome": "Rafaelle", "idade": "33", 
     "posicao": "Defensor", 
     "nascimento": "4", 
     "foto": "jogadora6.jpg"},
    
    {"nome": "Adriana", "idade": "36", 
     "posicao": "Meio-campo", 
     "nascimento": "5", 
     "foto": "jogadora9.jpg"},
    
    {"nome": "Kerolin", "idade": "24", 
     "posicao": "Atacante", 
     "nascimento": "6", 
     "foto": "jogadora4.jpg"},
    
    {"nome": "Debinha", "idade": "33", 
     "posicao": "Atacante", 
     "nascimento": "7", 
     "foto": "jogadora3.jpg"},
    
    {"nome": "Beatriz", "idade": "30", 
     "posicao": "Atacante", 
     "nascimento": "8", 
     "foto": "jogadora2.jpg"},
    
    {"nome": "Antonia", "idade": "30", 
     "posicao": "Defensor", 
     "nascimento": "9", 
     "foto": "jogadora1.jpg"},
    
    {"nome": "Gabriela Nunes", "idade": "27", 
     "posicao": "Atacante", 
     "nascimento": "10", 
     "foto": "jogadora11.jpg"},
    
    {"nome": "Monica", "idade": "37", 
     "posicao": "Meio-campo", 
     "nascimento": "11", 
     "foto": "jogadora10.jpg"},

    ]

    context = {
        "jogadores": jogadores_list,
    }

    return render(request, "jogadores.html")

def sobre(request):
    return render(request, "sobre.html")