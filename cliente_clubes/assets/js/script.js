const get_jugadores = async () => {
    let response = await fetch("http://localhost:8000/api/v1/jugadores")
    let data = await response.json()
    return data
}


// const btn_get_jugadores = document.getElementById("btn_get_jugadores")

// btn_get_jugadores.addEventListener("click", async ()=> {
//     let jugadores = await get_jugadores()

//     let liJugadores = ""
//     jugadores.forEach(jugador => {
//         liJugadores += `<li>Nombre: ${jugador.nombre} - Club: ${jugador.club}</li>`
//     })

//     lista_jugadores.innerHTML = liJugadores
// })

const recarga_jugadores = async () => {
    let jugadores = await get_jugadores()

    let filas = ""
    jugadores.forEach(jugador => {
        filas += `
                <tr>
                    <th scope="row">${jugador.id}</th>
                    <td>${jugador.nombre}</td>
                    <td>${jugador.club}</td>
                    <td>
                        <button class="btn btn-danger" onclick="eliminarJugador(${jugador.id})">Eliminar</button>
                    </td>
                </tr>
        `
    })

    cuerpoTabla.innerHTML = filas
}


const cuerpoTabla = document.querySelector("#listado_jugadores tbody")
document.addEventListener('DOMContentLoaded', () => {
    recarga_jugadores()
})


const eliminarJugador = async (id) => {
    let confirmacion = confirm("Está seguro que desea eliminar al jugador con ID: " + id)

    if(confirmacion){
        console.log("Eliminando jugador...")

        const requestOptions = {
            method: "DELETE",
            redirect: "follow",
            
        };
          
        let response = await fetch("http://localhost:8000/api/v1/jugadores/delete/"+id, requestOptions)
        
        if(response.status == 200){
            let data = await response.json();
            alert(data.message)
            recarga_jugadores()
        }
        else if(response.status == 404){
            alert("No existe un jugador con ID: " + id)
        }
        else {
            alert("Error al intentar eliminar al jugador")
        }
        
    }
}


const form_add_jugador = document.getElementById("form_add_jugador")

form_add_jugador.addEventListener("submit", async (event) => {
    event.preventDefault()

    const myHeaders = new Headers();
    myHeaders.append("Content-Type", "application/json");

    let data_form = new FormData(form_add_jugador)

    const raw = JSON.stringify({
        "nombre": data_form.get("nombre"),
        "apellido": data_form.get("apellido"),
        "dorsal": parseInt(data_form.get("dorsal")),
        "posicion": data_form.get("posicion"),
        "club": parseInt(data_form.get("club"))
    });

    const requestOptions = {
        method: "POST",
        headers: myHeaders,
        body: raw,
        redirect: "follow"
    };

    let response = await fetch("http://localhost:8000/api/v1/jugadores/add", requestOptions)

    if(response.status == 200){
        let data = await response.json()
        alert(data.message)
        form_add_jugador.reset()
        recarga_jugadores()
    }else{
        alert("Algo ha salido mal al momento de crear al jugador.")
    }

})