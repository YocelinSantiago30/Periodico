from django.contrib.auth import get_user_model
from django.test import TestCase

# Create your tests here.
class PruebasUsuarioPersonalizado(TestCase):
    def test_crear_usuario(self):
        Usuario = get_user_model()
        usuario = Usuario.objects.create_user(
            username="ana", email="ana@ejemplo.mx", password="Clave-segura-2026", edad=20
        )
        self.assertEqual(usuario.username, "ana")
        self.assertEqual(usuario.email, "ana@ejemplo.mx")
        self.assertEqual(usuario.edad, 20)
        self.assertTrue(usuario.is_active)
        self.assertFalse(usuario.is_staff)
        self.assertFalse(usuario.is_superuser)

    def test_crear_superusuario(self):
        Usuario = get_user_model()
        admin = Usuario.objects.create_superuser(
            username="jefa", email="jefa@ejemplo.mx", password="Clave-segura-2026"
        )
        self.assertEqual(admin.username, "jefa")
        self.assertEqual(admin.email, "jefa@ejemplo.mx")
        self.assertIsNone(admin.edad)
        self.assertTrue(admin.is_active)
        self.assertTrue(admin.is_staff)
        self.assertTrue(admin.is_superuser)