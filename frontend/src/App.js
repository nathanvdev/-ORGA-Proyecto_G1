import React, { useState } from "react";
import "bootstrap/dist/css/bootstrap.min.css";

const styles = {
  cyan: {
    backgroundColor: "#00FFFF",
    color: "black",
  },
  magenta: {
    backgroundColor: "#FF00FF",
    color: "black",
  },
  yellow: {
    backgroundColor: "#FFFF00",
    color: "black",
  },
  black: {
    backgroundColor: "black",
    color: "white",
  },
};

function App() {
  const [board, setBoard] = useState(
    Array(3)
      .fill(null)
      .map(() => Array(3).fill({ color: null, shape: null }))
  );
  const [selectedColor, setSelectedColor] = useState("black");
  const [selectedShape, setSelectedShape] = useState("");
  const [isFileMenuOpen, setIsFileMenuOpen] = useState(false);
  const [fileContent, setFileContent] = useState("");

  const handleCellClick = (rowIndex, colIndex) => {
    setBoard((prevBoard) => {
      const newBoard = [...prevBoard];
      const cell = newBoard[rowIndex][colIndex];
      if (cell.shape === null) {
        // Only update if the cell is empty
        newBoard[rowIndex][colIndex] = {
          color: selectedColor,
          shape: selectedShape,
        };
      }
      return newBoard;
    });
  };

  const handleColorSelection = (color) => {
    setSelectedColor(color);
  };

  const handleShapeSelection = (shape) => {
    setSelectedShape(shape);
  };

  const toggleFileMenu = () => {
    setIsFileMenuOpen(!isFileMenuOpen);
  };

  const NewFile= () => {
    setFileContent('');
  };

  const handleOpenFile = (event) => {
    const file = event.target.files[0];
    const reader = new FileReader();
    reader.onload = function (event) {
      setFileContent(event.target.result);
    };
    reader.readAsText(file);
  };

  const handleSaveFile = () => {
    const fileName = prompt("Please enter the file name");
    if (fileName) {
      const element = document.createElement("a");
      const file = new Blob([fileContent], {type: 'text/plain'});
      element.href = URL.createObjectURL(file);
      element.download = `${fileName}.orga`; // Always use .orga extension
      document.body.appendChild(element);
      element.click();
    }
  };

  const handleSubmit = () => {
    fetch("http://localhost:5000/sendData", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ code_in: fileContent }),
    })
      .then((response) => {
        if (!response.ok) {
          throw new Error("Error al enviar los datos al servidor");
        }
        return response.json();
      })
      .then((data) => {
        console.log("Respuesta del servidor:", data);
        // Aquí puedes manejar la respuesta del servidor según tus necesidades
      })
      .catch((error) => {
        console.error("Error:", error);
        // Aquí puedes manejar errores de solicitud o del servidor
      });
  };

  return (
    <div className="container" >
      <div className="container">
        <div className="row mt-3">
          {/* File Options Menu */}
          <div className="col d-flex justify-content-start align-items-center">
            <div className="dropdown">
              <button
                className="btn btn-secondary dropdown-toggle"
                type="button"
                onClick={toggleFileMenu}
              >
                Archivo
              </button>
              {isFileMenuOpen && (
                <ul
                  className="dropdown-menu show"
                  style={{ position: "absolute" }}
                >
                  <li>
                    <input
                      type="file"
                      className="dropdown-item"
                      onChange={handleOpenFile}
                      accept=".orga"
                    />
                  </li>
                  <li>
                    <a 
                      className="dropdown-item" 
                      href="#"
                      onClick={NewFile}
                      >
                      Nuevo archivo
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" 
                      href="#"
                      onClick={handleSaveFile}
                      >
                      Guardar
                    </a>
                  </li>
                  <li>
                    <a
                      className="dropdown-item"
                      href="#"
                      onClick={handleSubmit}
                    >
                      Imprimir
                    </a>
                  </li>
                  <li>
                    <a className="dropdown-item" href="#">
                      Salir
                    </a>
                  </li>
                </ul>
              )}
            </div>

            {/* Help Button */}
            <button
              className="btn btn-secondary"
              style={{ marginLeft: "10px" }}
            >
              Ayuda
            </button>
          </div>
        </div>
      </div>

      <div className="row mt-3">
        <div className="col">
          <textarea
            className="form-control"
            rows="3"
            value={fileContent}
            onChange={(e) => setFileContent(e.target.value)}
            style={{
              height:"150px",
              width: "100%",
              minHeight: "100px",
              backgroundColor: "#969ba5",
              color: "white",
              border: "10px solid #000000",
            }}
          />
        </div>
      </div>

      <div className="row mt-3" style={{ height: "500px" }}>
        <div className="col-9" style={{ height: "100%" }}>
          <div className="d-flex flex-column h-100">
            {board.map((row, rowIndex) => (
              <div key={rowIndex} className="d-flex flex-grow-1">
                {row.map((cell, colIndex) => (
                  <div
                    key={colIndex}
                    className="p-2 border text-center flex-grow-1 d-flex align-items-center justify-content-center"
                    style={{
                      backgroundColor: cell.color || "white",
                      fontSize: "2rem",
                      border: "5px solid #000000",
                      margin: "1px", 
                    }}
                    onClick={() => handleCellClick(rowIndex, colIndex)}
                  >
                    {cell.shape}
                  </div>
                ))}
              </div>
            ))}
          </div>
        </div>
        <div className="col-3">
          <div className="figuras-container" >
            <br></br>
            <label style={{ fontSize: 'larger', fontWeight: 'bold' }}>Figuras</label>
            {/* Shape Selection */}
            <div className="container">
              <div className="row mt-3">
                <div className="col" style={{ backgroundColor: "#cdd2d7", padding: "5px" }}>
                  {/* Botones */}
                  <button
                    className="btn btn-secondary mb-2 w-100"
                    style={{ backgroundColor: "#cdd2d7", color: "black" }}
                    onClick={() => handleShapeSelection("▲")}
                  >
                    &#9650;
                  </button>
                  <button
                    className="btn btn-secondary mb-2 w-100"
                    style={{ backgroundColor: "#cdd2d7", color: "black" }}
                    onClick={() => handleShapeSelection("○")}
                  >
                    &#9675;
                  </button>
                  <button
                    className="btn btn-secondary mb-2 w-100"
                    style={{ backgroundColor: "#cdd2d7", color: "black" }}
                    onClick={() => handleShapeSelection("×")}
                  >
                    &#215;
                  </button>
                  <button
                    className="btn btn-secondary mb-2 w-100"
                    style={{ backgroundColor: "#cdd2d7", color: "black" }}
                    onClick={() => handleShapeSelection("★")}
                  >
                    &#11088;
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div>
            <br></br>
            <label style={{ fontSize: 'larger', fontWeight: 'bold' , }}>Colores</label>
            {/* Color Selection */}
            <div style={{ backgroundColor: "#cdd2d7", padding: "10px" }}>
            <button
              className="btn w-100 mb-1"
              style={styles.cyan}
              onClick={() => handleColorSelection("cyan")}
            >
              Cyan
            </button>
            <button
              className="btn w-100 mb-1"
              style={styles.magenta}
              onClick={() => handleColorSelection("magenta")}
            >
              Magenta
            </button>
            <button
              className="btn w-100 mb-1"
              style={styles.yellow}
              onClick={() => handleColorSelection("yellow")}
            >
              Amarillo
            </button>
            <button
              className="btn w-100"
              style={styles.black}
              onClick={() => handleColorSelection("black")}
            >
              Negro
            </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default App;
