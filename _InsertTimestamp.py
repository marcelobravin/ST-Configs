import sublime, sublime_plugin, datetime

class InsertTimestampCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    sel = self.view.sel();
    for s in sel:
      agora   = datetime.datetime.now()
      #mascara = '%Y/%m/%d %H:%M:%S'
      mascara = '%d/%m/%Y %H:%M:%S'
      tempo   = datetime.datetime.strftime(agora, mascara)
      self.view.replace(edit, s, tempo)
      # self.view.erase(edit, region)
