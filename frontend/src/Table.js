import React, { useEffect, useState } from "react";
import axios from "axios";
import "bootstrap/dist/css/bootstrap.min.css";
import LevelDrop from "./LevelDrop";
import TableDrop from "./TableDrop";
import "./table_style.css";
import Paper from "@mui/material/Paper";
import { Box } from "@mui/material";

function Tablee() {
  const [level, setLevel] = useState("1");
  const [table, setTable] = useState(
    "bruftoinlandsprodukt_in_jeweiligen_preisen"
  );
  const [data, setData] = useState([]);
  const [metadata, setMetadata] = useState([]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/${table}/${level}`)
      .then((response) => {
        if (response.data.status === "success") {
          const parsedData = JSON.parse(response.data.data);
          setData(parsedData);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [table, level]);

  useEffect(() => {
    axios
      .get(`http://127.0.0.1:5000/api/${table}/metadata`)
      .then((response) => {
        if (response.data.status === "success") {
          const parsedData = JSON.parse(response.data.metadata);
          setMetadata(parsedData);
        }
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, [table]);

  const headers = data.length > 0 ? Object.keys(data[0]) : [];

  // Sort headers: string-based headers first
  const sortedHeaders = headers.sort((a, b) => {
    const isAString = isNaN(a);
    const isBString = isNaN(b);
    if (isAString && !isBString) return -1;
    if (!isAString && isBString) return 1;
    return 0;
  });

  return (
    <div className="container mt-3">
      <div className="row">
        <div className="col-6">
          <TableDrop table={table} setTable={setTable} />
        </div>
        <div className="col-6">
          <LevelDrop level={level} setLevel={setLevel} />
        </div>
        <div className="col-12">
            <Paper elevation={2} sx={{ padding: 1, marginTop: 2}}>
                <Box paddingLeft={2}>
                  <p style={{ margin: '0' }}>{metadata[0]}</p>
                  <p style={{ margin: '0' }}>{metadata[1]}</p>
                  <p style={{ margin: '0' }}>{metadata[2]}</p>
                </Box>
            </Paper>
        </div>
        <div className="col-12" style={{margin: "15px 0px 0px 0px"}}>
          <div
            className="table-responsive"
            style={{ maxHeight: "890px", overflowY: "scroll" }}
          >
            <table className="table table-striped table-hover">
              <thead className="table-light">
                <tr>
                  {sortedHeaders.map((header) => (
                    <th key={header}>{header}</th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {data.map((row, index) => (
                  <tr key={index}>
                    {sortedHeaders.map((header) => (
                      <td key={`${index}-${header}`}>{row[header]}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </div>
      </div>
    </div>
  );
}

export default Tablee;
