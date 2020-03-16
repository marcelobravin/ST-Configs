import sublime
import sublime_plugin
#import base64
#import os
#import re
#import urllib.parse
#import urllib.request
#import tempfile
#from . import get_image_size
# from pprint import pprint
import pprint


windowSidebarVisible = False

def dump(obj):
    for attr in dir(obj):
        if hasattr( obj, attr ):
            print( "obj.%s = %s" % (attr, getattr(obj, attr)))
    return

class HoverPreview(sublime_plugin.EventListener):



################################################################################

    # def read_pref_user():
    #     vis = userSettings.get('reveal-on-activate')
    #     if vis is not None:
    #         global pluginPref
    #         pluginPref = vis


    # def read_pref_package():
    #     vis = packageSettings.get('reveal-on-activate')
    #     if vis is not None:
    #         global pluginPref
    #         pluginPref = vis

    #userSettings = sublime.load_settings('Preferences.sublime-settings')
    # packageSettings = sublime.load_settings('SyncedSideBar.sublime-settings')

    # listen for changes
    # userSettings.add_on_change('Preferences', read_pref_user)
    # packageSettings.add_on_change('SyncedSideBar', read_pref_package)

    # read initial setting
    # read_pref_package()
    #read_pref_user()



################################################################################




    def on_window_command(self, window, command_name, args):
        if command_name == 'toggle_side_bar':
            global windowSidebarVisible
            windowSidebarVisible = not windowSidebarVisible

        # if close (fecha)

    def on_hover(self, view, point, hover_zone):

        # print('---------------------------')
        # dump(self)
        # dump(view)
        # dump(point)
        # dump(hover_zone)

        # pprint( vars(self) )
        # pprint( vars(view) )
        # pprint( vars(point) )
        # pprint( vars(hover_zone) )

        # pp = pprint.PrettyPrinter(indent=4)
        # pp.pprint( self )
        # pp.pprint( view )
        # pp.pprint( point )
        # pp.pprint( hover_zone )


        #sublime.status_message('---------------')
        #sublime.status_message('<div>%s</div>' % (hover_zone))
        # view.window().log("dsfsdfsdf");


        if hover_zone == sublime.HOVER_TEXT: # 1: texto
            # view.show_popup(
            #     '<div>%s</div>' % (hover_zone),
            #     flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
            #     location=point, # onde aparece
            #     max_width=view.viewport_extent()[0], # largura da janela
            #     max_height=view.viewport_extent()[1] # altura da janela
            #     )

            # view.run_command("show_scope_name")
            # view.window().run_command("hide_panel", {"cancel": True})

            # view.run_command("goto_line", {"line": 10})
            # view.run_command('insert_snippet', {"contents": "<$SELECTION>"})
            # view.window().run_command("prompt_select_project")
            # sublime.status_message('Running ' + ' '.join(cmd))
            # view.run_command("goto_line", {"line": point}) ## identificar linha apontada pelo mouse

            # sublime.status_message('Janela')

            # file_name = view.file_name()
            # sublime.status_message('%s' % file_name)

            # if windowSidebarVisible[view.window().id()]:
            if windowSidebarVisible:
                if view.window():
                    view.window().run_command("toggle_side_bar")
                else:
                    sublime.status_message("No window, can't show sidebar")
            # else:
                # sublime.status_message("Sidebar already hidden")

            return

        if hover_zone == 2: # gutter
            # view.show_popup(
                # '<div>%s</div>' % (hover_zone),
                # flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                # location=point, # onde aparece
                # max_width=view.viewport_extent()[0],
                # max_height=view.viewport_extent()[1]
                # )

            # view.window().run_command("show_overlay", {"overlay": "goto", "text": "@"})
            # sublime.status_message('Gutter')

            # if windowSidebarVisible[view.window().id()]:
            if not windowSidebarVisible:
                if view.window():
                    view.window().run_command("toggle_side_bar")
                    view.window().run_command("focus_side_bar")
                    view.window().run_command("hide_panel") # ------------------------ painel console, ctrl +f
                    view.window().run_command("hide_popup")
                else:
                    sublime.status_message("No window, can't show sidebar")
            # else:
                # sublime.status_message("Sidebar already opened")

            return

        if hover_zone == 3: # vazio
            # view.show_popup(
                # '<div>%s</div>' % (hover_zone),
                # flags=sublime.HIDE_ON_MOUSE_MOVE_AWAY,
                # location=point, # onde aparece
                # max_width=view.viewport_extent()[0],
                # max_height=view.viewport_extent()[1]
                # )

            # view.window().run_command("show_overlay", {"overlay": "goto"})
            # view.window().show_input_panel("File Name", "placeholder", "self.save", None, None);
            # view.window().run_command("show_overlay", {"overlay": "goto", "text": "#"})
            # view.window().run_command("show_overlay", {"overlay": "goto", "text": ":"})
            # view.window().run_command("show_overlay", {"overlay": "goto", "text": "@"})
            # sublime.status_message('Vazio')

            # if windowSidebarVisible[view.window().id()]:
            if windowSidebarVisible:
                if view.window():
                    view.window().run_command("toggle_side_bar")
                    # sublime.status_message("%s" % view.window().id() )
                else:
                    sublime.status_message("No window, can't show sidebar")
            # else:
                # sublime.status_message("Sidebar already hidden")


            return

        return



