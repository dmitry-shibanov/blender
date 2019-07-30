import bpy
from bpy.props import *
from .. base import BParticlesNode
from .. node_builder import NodeBuilder

class ParticleTrailsNode(bpy.types.Node, BParticlesNode):
    bl_idname = "bp_ParticleTrailsNode"
    bl_label = "Particle Trails"

    particle_type_name: StringProperty()

    def declaration(self, builder: NodeBuilder):
        builder.fixed_input("rate", "Rate", "Float", default=10)
        builder.particle_effector_output("effect", "Effect")

    def draw(self, layout):
        layout.prop(self, "particle_type_name", text="", icon="MOD_PARTICLES")
