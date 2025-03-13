from django.contrib.auth import get_user_model
from biblioteca.models import Llengua, Llibre, Exemplar, Usuari
from django.utils.timezone import now
import random
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'Seeds the database with initial data'
    
    def handle(self, *args, **options):
        # Inicializar Faker para diferentes idiomas
        fakers = {
            "Català": Faker('es_ES'),
            "Castellano": Faker('es_ES'),
            "English": Faker('en_US'),
            "Français": Faker('fr_FR'),
        }
        
        # Faker genérico para datos que no necesitan variar por idioma
        fake = Faker()
        User = get_user_model()
        
        self.stdout.write('Clearing existing data...')
        # Eliminar todos los libros anteriores
        Llibre.objects.all().delete()
        Exemplar.objects.all().delete()
        Usuari.objects.all().delete()
        Llengua.objects.all().delete()
        
        self.stdout.write('Creating languages...')
        # Crear lenguas
        llengues = {
            "Català": Llengua.objects.create(nom="Català"),
            "Castellano": Llengua.objects.create(nom="Castellano"),
            "English": Llengua.objects.create(nom="English"),
            "Français": Llengua.objects.create(nom="Français"),
        }
        
        self.stdout.write('Creating books...')
        # Crear libros
        llibres = []
        for llengua_nom, llengua_obj in llengues.items():
            # Usar el faker específico para este idioma
            lang_faker = fakers[llengua_nom]
            for _ in range(10):
                llibre = Llibre.objects.create(
                    titol=lang_faker.sentence(nb_words=4),
                    autor=lang_faker.name(),
                    data_edicio=fake.date_this_century(),
                    llengua=llengua_obj,
                    ISBN=fake.isbn13(),
                    editorial=lang_faker.company(),
                    pagines=random.randint(100, 1000),
                )
                llibres.append(llibre)
        
        self.stdout.write('Creating copies...')
        # Crear ejemplares (2 por libro)
        for llibre in llibres:
            for _ in range(2):
                Exemplar.objects.create(cataleg=llibre, registre=fake.uuid4())
        
        self.stdout.write('Creating users...')

        # Crear usuarios
        for _ in range(50):
            Usuari.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                password="password123",
                first_name=fake.first_name(),
                last_name=fake.last_name(),
            )
            
        # Crear superusuario
        self.stdout.write('Creating superuser (admin/123)...')
        User.objects.filter(username='admin').delete()
        User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='123',
            first_name='Admin',
            last_name='User'
        )
            
        self.stdout.write(self.style.SUCCESS('Datos insertados correctamente.'))
