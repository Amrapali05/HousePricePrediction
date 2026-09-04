# #from django.shortcuts import render

# # def home(request):
# #     prediction = None

# #     if request.method == "POST":
# #         area = int(request.POST['area'])
# #         bedrooms = int(request.POST['bedrooms'])
# #         bathrooms = int(request.POST['bathrooms'])

# #         prediction = (area * 5000) + (bedrooms * 100000) + (bathrooms * 50000)

# #     return render(request, 'home.html', {'prediction': prediction})
# # 
# from django.shortcuts import render
# from .models import HousePrediction

# def home(request):
#     prediction = None

#     if request.method == "POST":
#         location = request.POST["location"]
#         sqft = int(request.POST["sqft"])
#         bhk = int(request.POST["bhk"])
#         bath = int(request.POST["bath"])

#         # Temporary prediction formula
#         prediction = (sqft * 500) + (bhk * 1000) + (bath * 500)

#         HousePrediction.objects.create(
#             location=location,
#             sqft=sqft,
#             bhk=bhk,
#             bath=bath,
#             price=prediction
#         )

#     return render(request, "home.html", {"prediction": prediction})
import os
import pickle
from django.shortcuts import render
from .models import HousePrediction

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

with open(os.path.join(BASE_DIR, "model", "house_model.pkl"), "rb") as f:
    model = pickle.load(f)

def home(request):
    prediction = None

    if request.method == "POST":
        location = request.POST["location"]
        sqft = int(request.POST["sqft"])
        bhk = int(request.POST["bhk"])
        bath = int(request.POST["bath"])

        prediction = model.predict([[sqft, bhk, bath]])[0]

        HousePrediction.objects.create(
            location=location,
            sqft=sqft,
            bhk=bhk,
            bath=bath,
            price=prediction
        )

    return render(request, "home.html", {"prediction": round(prediction, 2) if prediction else None})