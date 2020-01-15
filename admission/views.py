from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import pandas as pd


def admission_client(request):
    return render(request, 'admission.html')


def predict_chances(request):
    # Receive data from client
    gre = int(request.GET['gre'])
    toefl = int(request.GET['toefl'])
    cgpa = float(request.GET['cgpa'])

    model = pd.read_pickle(r"C:\Users\Admin\Desktop\Boulot 4A\Projet Python\deploying_model\lr_model.pickle")
    chances = model.predict([[gre, toefl, cgpa]])
    return HttpResponse(f"{chances[0] * 100:.2f}%")