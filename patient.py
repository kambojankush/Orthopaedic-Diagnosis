import json

class Patient:

    def __init__(self, cpf, name, address, telephone, email):
        self.cpf = cpf
        self.name = name
        self.address = address
        self.telephone = telephone
        self.email = email

    @classmethod
    def from_input(cls):
        return cls(
            input('CPF: '),
            input('NAME: '),
            input('Address: '),
            input('Telephone: '),
            input('Email: ')
            )


class VertebralColumnReport:
    def __init__(self, patient, report):
        self.id = patient
        self.pelvic_incidence = report['pelvic_incidence']
        self.pelvic_tilt = report['pelvic_tilt']
        self.lumbar_lordosis_angle = report['lumbar_lordosis_angle']
        self.sacral_slope = report['sacral_slope']
        self.pelvic_radius = report['pelvic_radius']
        self.grade_of_spondylolisthesis = report['grade_of_spondylolisthesis']

    def tolist(self):
        return [self.pelvic_incidence,
            self.pelvic_tilt,
            self.lumbar_lordosis_angle,
            self.sacral_slope,
            self.pelvic_radius,
            self.grade_of_spondylolisthesis]

    def todict(self):
        return {
            'pelvic_incidence' : self.pelvic_incidence,
            'pelvic_tilt' : self.pelvic_tilt,
            'lumbar_lordosis_angle' : self.lumbar_lordosis_angle,
            'sacral_slope' : self.sacral_slope,
            'pelvic_radius' : self.pelvic_radius,
            'grade_of_spondylolisthesis' : self.grade_of_spondylolisthesis
        }
