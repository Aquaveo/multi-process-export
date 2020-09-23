"""Script to export a Standard Interface Template geometry file."""
# 1. Standard python modules

# 2. Third party modules

# 3. Aquaveo modules

# 4. Local modules


if __name__ == "__main__":
    import os
    from xmsapi.dmi import Query
    from standard_interface_template.components.sim_query_helper import SimQueryHelper
    from standard_interface_template.file_io.geometry_writer import GeometryWriter

    query = Query()
    query.get_xms_agent().set_retries(1)
    r = query.get('simulation_name')
    simulation_name = r['simulation_name'][0].get_as_string()
    query.select('StandardInterfaceTemplate#Sim_Manager')

    sim_query_helper = SimQueryHelper(query)
    sim_query_helper.get_geometry(False)

    path = os.getcwd()
    base_name = f'{simulation_name}.example_geometry'
    file_name = os.path.join(path, base_name)
    writer = GeometryWriter(file_name=file_name, grid=sim_query_helper.co_grid.ugrid)
    writer.write()
