import sublime, sublime_plugin

class RemoveCaracteresCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        sel = self.view.sel()
        for s in sel:
            s2 = self.view.substr(s)

            caracteres=[
                ['a', 'á'],
                ['A', 'Á'],
                ['e', 'é'],
                ['E', 'É'],
                ['i', 'í'],
                ['I', 'Í'],
                ['o', 'ó'],
                ['O', 'Ó'],
                ['u', 'ú'],
                ['U', 'Ú'],
                ['c', 'ç'],
                ['C', 'Ç'],
                ['n', 'ñ'],
                ['N', 'Ñ'],
                ['a', 'ã'],
                ['A', 'Ã'],
                ['o', 'õ'],
                ['O', 'Õ'],
                ['i', 'ì'],
                ['I', 'Ì'],
                ['a', 'à'],
                ['A', 'À'],
                ['o', 'ô'],
                ['O', 'Ô'],
                ['a', 'â'],
                ['A', 'Â'],
                ['e', 'ê'],
                ['E', 'Ê'],
            ]

            x = range( len(caracteres) )
            for i in x:
                pos = s2.find(caracteres[i][0])
                if pos != -1:
                    s2 = s2.replace(caracteres[i][1], caracteres[i][0])
                    self.view.replace(edit, s, s2)
