from django.db import models


# Create your models here.
class Direction(models.Model):
    street = models.CharField(max_length=50, verbose_name='Calle')
    city = models.CharField(max_length=50, verbose_name='Ciudad')
    country = models.CharField(max_length=50, verbose_name='Pais')
    municipality = models.CharField(max_length=50, verbose_name="Municipio")
    cp = models.CharField(max_length=10, verbose_name="Código Postal")
    ext = models.CharField(max_length=10, verbose_name="No. Exterior")
    int = models.CharField(max_length=10, verbose_name='No. Interior')

    def __str__(self):
        return "Dirección: {0} {1}".format(self.street, self.ext)

    class Meta:
        verbose_name = "Dirección"
        verbose_name_plural = "Direcciones"


class Person(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    address = models.ForeignKey(Direction, on_delete=models.CASCADE, verbose_name='Dirección')
    birthday = models.DateTimeField()
    age = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='Edad')
    weight = models.DecimalField(max_digits=4, decimal_places=2, verbose_name="Peso")
    height = models.DecimalField(max_digits=3, decimal_places=2, verbose_name="Altura")
    phone = models.CharField(max_length=10, verbose_name="Teléfono")
    cur = models.CharField(max_length=18, verbose_name="CURP")
    rfc = models.CharField(max_length=12, verbose_name="RFC")
    sex = models.CharField(max_length=1, verbose_name="Sexo")

    def __str__(self):
        return "Persona: {0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name = "Persona"
        verbose_name_plural = "Personas"


class Medic(models.Model):
    firstname = models.CharField(max_length=50, verbose_name='Nombre')
    lastname = models.CharField(max_length=50, verbose_name='Apellidos')
    age = models.DecimalField(max_digits=3, decimal_places=0, verbose_name='Edad')
    phone = models.CharField(max_length=10, verbose_name="Teléfono")
    cur = models.CharField(max_length=18, verbose_name="CURP")
    rfc = models.CharField(max_length=12, verbose_name="RFC")
    sex = models.CharField(max_length=1, verbose_name="Sexo")
    cedula = models.CharField(max_length=10, verbose_name='cedula')

    def __str__(self):
        return "Médico: {0} {1}".format(self.firstname, self.lastname)

    class Meta:
        verbose_name = "Médico"
        verbose_name_plural = "Médicos"


class Cite(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE, verbose_name='Médico')
    date = models.DateTimeField()

    def __str__(self):
        return "Cita: {0} {1}".format(self.person, self.date)

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"


class Diagnosis(models.Model):
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE, verbose_name='Médico')
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    diagnosis = models.CharField(max_length=100, verbose_name='Diagnóstico')
    date = models.DateTimeField()

    def __str__(self):
        return "Diagnóstico: {0} {1}".format(self.person, self.diagnosis)

    class Meta:
        verbose_name = "Diagnóstico"
        verbose_name_plural = "Diagnósticos"


class Diet(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE, verbose_name='Médico')
    diet = models.CharField(max_length=100, verbose_name='Dieta')
    date = models.DateTimeField()

    def __str__(self):
        return "Dieta: {0} {1}".format(self.person, self.diet)

    class Meta:
        verbose_name = "Dieta"
        verbose_name_plural = "Dietas"


class Allergy(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    allergy = models.CharField(max_length=50, verbose_name='Alergia')

    def __str__(self):
        return "Alergia: {0} {1}".format(self.person, self.allergy)

    class Meta:
        verbose_name = "Alergia"
        verbose_name_plural = "Alergias"


class Record(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    medic = models.ForeignKey(Medic, on_delete=models.CASCADE, verbose_name='Médico')
    diagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE, verbose_name='Diagnóstico')
    allergy = models.ForeignKey(Allergy, on_delete=models.CASCADE, verbose_name='Alergia')
    diet = models.ForeignKey(Diet, on_delete=models.CASCADE, verbose_name='Dieta')

    def __str__(self):
        return "Historial: {0}".format(self.person)

    class Meta:
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"


class Laboratory(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE, verbose_name='Paciente')
    laboratory = models.CharField(max_length=50, verbose_name='Laboratorio')
    date = models.DateTimeField()

    def __str__(self):
        return "Laboratorio: {0} {1}".format(self.person, self.laboratory)

    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"