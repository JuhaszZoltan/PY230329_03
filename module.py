class Versenyzo:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szul_ev:int = int(v[1])
        self.rajtszam:int = int(v[2])
        self.nem:bool = v[3] == 'f'
        self.kategoria:str = v[4]
        self.idoeredmenyek:dict[str, str] = {
            'úszás': v[5],
            'I. depó': v[6],
            'kerékpár': v[7],
            'II. depó': v[8],
            'futás': v[9]
        }
        self.ossz_mp:int = 0
        for ie in self.idoeredmenyek.values():
            opm:list[str] = ie.split(':')
            o:int = int(opm[0])
            p:int = int(opm[1])
            m:int = int(opm[2])
            self.ossz_mp += (o * 3600 + p * 60 + m)
