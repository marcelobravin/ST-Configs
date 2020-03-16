#http://code.tutsplus.com/tutorials/how-to-create-a-sublime-text-2-plugin--net-22685
# TODO: separar caracteres|símbolos|todos, codificar|decodificar
import sublime, sublime_plugin

class CaracteresCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        for s in sel:
            s2 = self.view.substr(s)

            caracteres=[
                ['&nbsp;', ' '],
                ['&aacute;', 'á'],
                ['&Aacute;', 'Á'],
                ['&eacute;', 'é'],
                ['&Eacute;', 'É'],
                ['&iacute;', 'í'],
                ['&Iacute;', 'Í'],
                ['&oacute;', 'ó'],
                ['&Oacute;', 'Ó'],
                ['&uacute;', 'ú'],
                ['&Uacute;', 'Ú'],
                ['&ccedil;', 'ç'],
                ['&Ccedil;', 'Ç'],
                ['&ntilde;', 'ñ'],
                ['&Ntilde;', 'Ñ'],
                ['&atilde;', 'ã'],
                ['&Atilde;', 'Ã'],
                ['&otilde;', 'õ'],
                ['&Otilde;', 'Õ'],
                ['&igrave;', 'ì'],
                ['&Igrave;', 'Ì'],
                ['&agrave;', 'à'],
                ['&Agrave;', 'À'],
                ['&ocirc;', 'ô'],
                ['&Ocirc;', 'Ô'],
                ['&acirc;', 'â'],
                ['&Acirc;', 'Â'],
                ['&ecirc;', 'ê'],
                ['&Ecirc;', 'Ê'],
                ['&gt;', '>'],
                ['&lt;', '<']
            ]

            x = range( len(caracteres) )
            for i in x:
                pos = s2.find(caracteres[i][0])
                if pos != -1:
                    s2 = s2.replace(caracteres[i][0], caracteres[i][1])
                    self.view.replace(edit, s, s2)
