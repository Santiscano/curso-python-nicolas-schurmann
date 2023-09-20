"""
Esta es el modulo que incluye el reproductor de musica
"""

class Player:
    """
    Esta clase crea un reproductor de musica
    """

    def play(self, song):
        """
        Reproduce la cancion que recibio como parametro

        Parameters:
        song: (str): este es un string con el path de la cancion

        Returns:
        int: devuelve 1 si reproduce con exito,  0 si genera un error
        """
        print("reproduciendo cancion", song)

    def stop(self):
        """
        esta no la documente por pereza
        """
        print('deteniendose')