from django import forms
from .models import TeamRegistration


class TeamRegistrationForm(forms.ModelForm):
    class Meta:
        model = TeamRegistration
        fields = [
            "team_name",
            "team_logo",
            "player1",
            "player1_riot_id",
            "player2",
            "player2_riot_id",
            "player3",
            "player3_riot_id",
            "player4",
            "player4_riot_id",
            "player5",
            "player5_riot_id",
            "player6",
            "player6_riot_id",
            "player7",
            "player7_riot_id",
            "registrant_email",
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        material_class = "w-full border border-gray-300 rounded-md p-2 focus:outline-none focus:ring-2 focus:ring-indigo-500"
        for field_name, field in self.fields.items():
            # Optionally, you can skip FileInput widgets if you prefer default styling:
            if field.widget.__class__.__name__ != "ClearableFileInput":
                field.widget.attrs.update({"class": material_class})
            else:
                field.widget.attrs.update({"class": "w-full text-gray-700"})
