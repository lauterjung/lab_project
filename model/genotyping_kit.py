from model.locus import Marker


class GenotypingKit():
    
    def __init__(self, name: str, codification: str, brand: str, number_of_dyes: int, markers: list[Marker]):
        self.name = name
        self.codification = codification
        self.brand = brand
        self.number_of_dyes = number_of_dyes
        self.markers = markers

kit_VE = GenotypingKit("VeriFiler_Express", "VE", "ThermoFischer", 6, 
        [Marker.D3S1358, Marker.vWA, Marker.D16S539, Marker.CSF1PO, Marker.TPOX, 
        Marker.Y_indel, Marker.AMEL, Marker.D8S1179, Marker.D21S11, Marker.D18S51,
        Marker.Penta_E, Marker.D2S441, Marker.D19S433, Marker.TH01, Marker.FGA,
        Marker.D22S1045, Marker.D5S818, Marker.D13S317, Marker.D7S820, Marker.D6S1043,
        Marker.D10S1248, Marker.D1S1656, Marker.D12S391, Marker.D2S1338, Marker.Penta_D])

kit_P6 = GenotypingKit("Powerplex...", "P6", "Promega", 6, 
        [Marker.AMEL, Marker.D3S1358, Marker.D1S1656, Marker.D2S441, Marker.D10S1248, 
        Marker.D13S317, Marker.Penta_E, Marker.D16S539, Marker.D18S51, Marker.D2S1338, 
        Marker.CSF1PO, Marker.Penta_D, Marker.TH01, Marker.vWA, Marker.D21S11, 
        Marker.D7S820, Marker.D5S818, Marker.TPOX, Marker.D8S1179, Marker.D12S391, 
        Marker.D19S433, Marker.SE33, Marker.D22S1045, Marker.DYS391, Marker.FGA, 
        Marker.DYS576, Marker.DYS570])

kit_C7 = GenotypingKit("C7....", "C7", "ThermoFischer", 3, 
        [Marker.LPL, Marker.F13B, Marker.FESFPS, Marker.F13A01, Marker.Penta_D, 
        Marker.Penta_C, Marker.Penta_E])

kit_XQ = GenotypingKit("Argus_X12_QS", "XQ", "Qiagen", 4, 
        [Marker.AMEL, Marker.DXS10103, Marker.DXS8378, Marker.DXS10101, Marker.DXS10134, 
        Marker.DXS10074, Marker.DXS7132, Marker.DXS10135, Marker.DXS7243, Marker.DXS10146, 
        Marker.DXS10079, Marker.HPRTB, Marker.DXS10148, Marker.D21S11])

kit_Y3 = GenotypingKit("Y3...", "Y3", "Promega", 1, 
        [])

kit_V7 = GenotypingKit("Versaplex...", "V7", "Promega", 6, 
        [Marker.AMEL, Marker.D3S1358, Marker.D1S1656, Marker.D2S441, Marker.D10S1248, 
        Marker.D13S317, Marker.Penta_E, Marker.D16S539, Marker.D18S51, Marker.D2S1338, 
        Marker.CSF1PO, Marker.Penta_D, Marker.TH01, Marker.vWA, Marker.D21S11, 
        Marker.D7S820, Marker.D5S818, Marker.TPOX, Marker.D8S1179, Marker.D12S391, 
        Marker.D19S433, Marker.D6S1043, Marker.D22S1045, Marker.DYS391, Marker.FGA, 
        Marker.DYS576, Marker.DYS570])