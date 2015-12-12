# ##### BEGIN GPL LICENSE BLOCK #####
#
#  This program is free software; you can redistribute it and/or
#  modify it under the terms of the GNU General Public License
#  as published by the Free Software Foundation; either version 2
#  of the License, or (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software Foundation,
#  Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.
#
# ##### END GPL LICENSE BLOCK #####

bl_info = {
    "name": "Material Library",
    "author": "Microvellum, Inc.",
    "version": (1, 0, 0),
    "blender": (2, 71, 0),
    "location": "View 3D>Tools Panel>Library",
    "warning": "",
    "description": "This is the base library that stores objects, materials, worlds, and groups",
    "wiki_url": "http://www.microvellum.com",
    "category": "Library Add-on",
    "fd_open_id":"materiallib.open",
    "fd_drop_id":"materiallib.drop",
    "icon":"MATERIAL",
}

import bpy

class PREFERENCES_Material_Library(bpy.types.AddonPreferences):
    bl_idname = __name__

    path = bpy.props.StringProperty(name="Path To Materials",
                                    default="",
                                    subtype='DIR_PATH')

    def draw(self, context):
        layout = self.layout
        layout.prop(self, "path")

def register():
    bpy.utils.register_class(PREFERENCES_Material_Library)
    
    from . import properties
    from . import ui
    from . import operators
    
    properties.register()
    ui.register()
    operators.register()

def unregister():
    bpy.utils.unregister_class(PREFERENCES_Material_Library)
    
    from . import properties
    from . import ui
    from . import operators
    
    properties.unregister()
    ui.unregister()
    operators.unregister()