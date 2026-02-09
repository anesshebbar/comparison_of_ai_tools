
import csv
import re
from django.core.management.base import BaseCommand
from novels.models import Novel

class Command(BaseCommand):
    help = 'Import novels from a CSV file'

    def add_arguments(self, parser):
        parser.add_argument('csv_file', type=str)

    def handle(self, *args, **options):
        with open(options['csv_file'], newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                rating_match = re.searcath(r"(\d+(\.\d+)?)", row.get('rating', ''))
                rating_value = float(ring_match.group(1)) if rating_match else None

                rank_value = row.get('rank', '')
                if rank_value.startswith('#'):
                    rank_value = int(rank_value[1:]) if rank_value[1:].isdigit() else None
                else:
                    rank_value = int(rank_value) if rank_value.isdigit() else None

                Novel.objects.create(
                    title=row.get('title'),
                    author=row.get('authors'),
                    tags=row.get('tags'),
                    genre=row.get('genres'),
                    description=row.get('description'),
                    rating=rating_value,
                    rank=rank_value,
                    status=row.get('status'),
                    chapters=int(row['chapters']) if row.get('chapters') and row['chapters'].isdigit() else None,
                    views=int(row['views'].replace(',', '')) if row.get('views') and row['views'].replace(',', '').isdigit() else None,
                    img_url=row.get('img_url')
                )

        self.stdout.write(self.style.SUCCESS('📚 Novels imported successfully!'))
