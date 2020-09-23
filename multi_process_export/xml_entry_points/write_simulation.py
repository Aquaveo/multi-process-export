"""Script to export a Standard Interface Template simulation file."""
# 1. Standard python modules

# 2. Third party modules

# 3. Aquaveo modules

# 4. Local modules


if __name__ == "__main__":
    import os
    from xmsapi.dmi import Query
    from standard_interface_template.components.sim_query_helper import SimQueryHelper
    from standard_interface_template.file_io.simulation_writer import SimulationWriter

    query = Query()
    query.get_xms_agent().set_retries(1)
    r = query.get('simulation_name')
    simulation_name = r['simulation_name'][0].get_as_string()

    sim_query_helper = SimQueryHelper(query)

    path = os.getcwd()
    base_name = f'{simulation_name}.example_simulation'
    files_exported = [f'Grid "{simulation_name}.example_geometry"',
                      f'Materials "{simulation_name}.example_materials"',
                      f'Boundary_Conditions "{simulation_name}.example_boundary"']
    file_name = os.path.join(path, base_name)
    writer = SimulationWriter(file_name=file_name, simulation_data=sim_query_helper.sim_component,
                              other_files=files_exported)
    writer.write()
