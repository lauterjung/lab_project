from enum import Enum
from msilib.schema import Class
from xml.sax.handler import feature_namespace_prefixes

class STR_Region (Enum):
    autossomic = 1
    x_chromossome = 2
    y_chromossome = 3
    
class Marker (Enum):
    CSF1PO = 1
    D1S1656 = 2
    D2S1338 = 3
    D2S441 = 4
    D3S1358 = 5
    D5S818 = 6
    D6S1043 = 7
    D7S820 = 8
    D8S1179 = 9
    D10S1248 = 10
    D12S391 = 11
    D13S317 = 12
    D16S539 = 13
    D18S51 = 14
    D19S433 = 15
    D21S11 = 16
    D22S1045 = 17
    F13A01 = 18
    F13B = 19
    FESFPS = 20
    FGA = 21
    LPL = 22
    Penta_C = 23
    Penta_D = 24
    Penta_E = 25
    SE33 = 26
    TH01 = 27
    TPOX = 28
    vWA = 29
    Y_indel = 30
    DXS10074 = 31 # H2
    DXS10079 = 32 # H2
    DXS10101 = 33 # H3
    DXS10103 = 34 # H3
    DXS10134 = 35 # H4
    DXS10135 = 36 # H1
    DXS10146 = 37 # H4
    DXS10148 = 38 # H1
    DXS7132 = 39 # H2
    DXS7243 = 40 # H4
    DXS8378 = 41 # H1
    HPRTB = 42 # H3
    DYS19 = 43
    DYS385 = 44
    DYS389_I = 45
    DYS389_II = 46
    DYS390 = 47
    DYS391 = 48
    DYS392 = 49
    DYS393 = 50
    DYS437 = 51
    DYS438 = 52
    DYS439 = 53
    DYS448 = 54
    DYS456 = 55
    DYS458 = 56
    DYS481 = 57
    DYS533 = 58
    DYS549 = 59
    DYS570 = 60
    DYS576 = 61
    DYS635 = 62
    DYS643 = 63
    YGATA_H4 = 64
    AMEL = 65

class Locus():
    alleles: dict[str, float]
    
    def __init__(self, name: str):
        self.name = name
        self.alleles = {}