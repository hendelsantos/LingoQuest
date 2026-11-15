from django.core.management.base import BaseCommand

from apps.learning.services import seed_a1_foundations


class Command(BaseCommand):
    help = "Cria ou atualiza o currículo demonstrativo A1 Foundations."

    def handle(self, *args, **options):
        totals = seed_a1_foundations()
        self.stdout.write(
            self.style.SUCCESS(
                "A1 Foundations pronto: "
                f"{totals['units']} unidades, {totals['lessons']} lições e "
                f"{totals['questions']} perguntas."
            )
        )
