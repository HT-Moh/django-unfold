from import_export.forms import ExportForm as BaseExportForm
from import_export.forms import ImportForm as BaseImportForm
from unfold.widgets import UnfoldAdminFileFieldWidget
from unfold.settings import get_config


class ImportForm(BaseImportForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["import_file"].widget = UnfoldAdminFileFieldWidget()
        self.fields["input_format"].widget.attrs["class"] = " ".join(get_config()["SELECT_CLASSES"])


class ExportForm(BaseExportForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["file_format"].widget.attrs["class"] = " ".join(get_config()["SELECT_CLASSES"])
