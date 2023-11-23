from django.shortcuts import render
from django.http import HttpResponse

def info (request, fio, age, hobby):
    return HttpResponse(f"<h1>фио: {fio}, <br> возраст: {age}, <br> интересы: {hobby}</h1>")

def about (request, city, school, teach):
    return HttpResponse(f"<h1>откуда приехала: {city}, <br> успеваемость в школе: {school}, <br> любите/не любите учиться: {teach}</h1>")

def contacts (request, github, tg, num):
    return HttpResponse(f'<h1>Гитхаб: {github}, <br> Телеграмм: {tg}, <br> номер телефона: {num}</h1>')
