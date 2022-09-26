from openroad import Tech, Design
import helpers

tech = Tech()
tech.readLEF("Nangate45/Nangate45.lef")
tech.readLiberty("Nangate45/Nangate45_typ.lib")

design = Design(tech)
design.readVerilog("reg1.v")
design.link("top")

space = design.micronToDBU(1)

floorplan = design.getFloorplan()
floorplan.initFloorplan(30,
                        0.5,
                        space, space, space, space,
                        "FreePDK45_38x28_10R_NP_162NW_34O")

def_file = helpers.make_result_file("init_floorplan2.def")
design.writeDef(def_file)
helpers.diff_files('init_floorplan2.defok', def_file)