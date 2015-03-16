import sublime_plugin


_tooltips_enabled = False


class SelectionListener(sublime_plugin.EventListener):

    def on_selection_modified(self, view):
        if _tooltips_enabled:
            if len(view.sel()) > 1:
                return

            sel = view.sel()[0]
            if sel.empty():
                text = "{}".format(sel.a)
            else:
                text = "({}, {})".format(sel.begin(), sel.end())

            view.show_popup(text)


class ToggleSelectionTooltips(sublime_plugin.ApplicationCommand):

    def run(self):
        global _tooltips_enabled
        _tooltips_enabled = not _tooltips_enabled
