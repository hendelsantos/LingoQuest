from django.core.management.base import BaseCommand

from apps.learning.services import seed_curriculum


class Command(BaseCommand):
    help = "Sincroniza o currículo completo (A1 a C2) definido em apps.learning.content."

    def handle(self, *args, **options):
        totals = seed_curriculum()
        self.stdout.write(
            self.style.SUCCESS(
                "Currículo pronto: "
                f"{totals['courses']} cursos, {totals['units']} unidades, "
                f"{totals['lessons']} lições, {totals['questions']} perguntas e "
                f"{totals['choices']} alternativas."
            )
        )
