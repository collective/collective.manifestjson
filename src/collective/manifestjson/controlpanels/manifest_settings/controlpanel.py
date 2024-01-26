# -*- coding: utf-8 -*-
from collective.manifestjson import _
from collective.manifestjson.interfaces import ICollectiveManifestjsonLayer
from plone.app.registry.browser.controlpanel import ControlPanelFormWrapper
from plone.app.registry.browser.controlpanel import RegistryEditForm
from plone.restapi.controlpanels import RegistryConfigletPanel
from plone.z3cform import layout
from zope import schema
from zope.component import adapter
from zope.interface import Interface


class IManifestSettings(Interface):
    myfield_name = schema.TextLine(
        title=_(
            "This is an example field for this control panel",
        ),
        description=_(
            "",
        ),
        default="",
        required=False,
        readonly=False,
    )


class ManifestSettings(RegistryEditForm):
    schema = IManifestSettings
    schema_prefix = "collective.manifestjson.manifest_settings"
    label = _("Manifest Settings")


ManifestSettingsView = layout.wrap_form(ManifestSettings, ControlPanelFormWrapper)


@adapter(Interface, ICollectiveManifestjsonLayer)
class ManifestSettingsConfigletPanel(RegistryConfigletPanel):
    """Control Panel endpoint"""

    schema = IManifestSettings
    configlet_id = "manifest_settings-controlpanel"
    configlet_category_id = "Products"
    title = _("Manifest Settings")
    group = ""
    schema_prefix = "collective.manifestjson.manifest_settings"
