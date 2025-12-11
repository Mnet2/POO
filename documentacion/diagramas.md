classDiagram
    %% Estilos para distinguir capas
    classDef dominio fill:#e1f5fe,stroke:#01579b;
    classDef persistencia fill:#fff9c4,stroke:#fbc02d;
    classDef aplicacion fill:#e8f5e9,stroke:#2e7d32;
    classDef presentacion fill:#f3e5f5,stroke:#7b1fa2;

    namespace Dominio {
        class Usuario {
            +username: str
            +password: str
            +rol: str
        }
        class Empleado {
            +id: int
            +nombre: str
            +salario: int
            +departamento_id: int
        }
        class Departamento {
            +id: int
            +nombre: str
            +gerente_id: int
        }
        class Proyecto {
            +id: int
            +nombre: str
            +fecha_inicio: date
        }
    }

    namespace Persistencia {
        class Conexion {
            -host: str
            -user: str
            -db: str
            +conectar()
            +desconectar()
        }
        class UsuarioDAO {
            +buscar_por_username()
            +agregar()
            +listar_todos()
        }
        class EmpleadoDAO {
            +agregar()
            +buscar_por_id()
            +mostrar_todos()
        }
        class DepartamentoDAO {
            +agregar()
            +mostrar_todos()
        }
        class ProyectoDAO {
            +agregar()
            +mostrar_todos()
        }
    }

    namespace Aplicacion {
        class ReglasUsuario {
            +login(user, pass)
            +crear_usuario()
        }
        class ReglasEmpleado {
            +registrar_empleado()
            +listar_empleados()
        }
        class ReglasDepartamento {
            +crear_departamento()
        }
    }

    namespace Presentacion {
        class MenuPrincipal {
            +mostrar_menu()
            +iniciar_login()
        }
    }

    %% Relaciones entre capas
    UsuarioDAO ..> Conexion : usa
    EmpleadoDAO ..> Conexion : usa
    
    ReglasUsuario --> UsuarioDAO : usa
    ReglasEmpleado --> EmpleadoDAO : usa
    ReglasDepartamento --> DepartamentoDAO : usa

    UsuarioDAO ..> Usuario : mapea
    EmpleadoDAO ..> Empleado : mapea

    MenuPrincipal --> ReglasUsuario : solicita lógica
    MenuPrincipal --> ReglasEmpleado : solicita lógica

    class Usuario:::dominio
    class Empleado:::dominio
    class UsuarioDAO:::persistencia
    class ReglasUsuario:::aplicacion
    class MenuPrincipal:::presentacion


    usecaseDiagram
    actor "Administrador" as admin
    actor "Empleado" as user

    package "Sistema de Gestión (Agencia/Empresa)" {
        usecase "Iniciar Sesión" as UC1
        usecase "Registrar Usuario" as UC2
        usecase "Gestionar Empleados" as UC3
        usecase "Asignar Departamento" as UC4
        usecase "Crear Proyecto" as UC5
        usecase "Ver Proyectos Asignados" as UC6
    }

    admin --> UC1
    admin --> UC2
    admin --> UC3
    admin --> UC4
    admin --> UC5

    user --> UC1
    user --> UC6