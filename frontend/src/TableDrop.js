import * as React from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

function TableDrop({table, setTable}) {
    const handleChange = (event) => {
        setTable(event.target.value);
    };
    return (
        <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">Table</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={table}
                label="Age"
                onChange={handleChange}
            >
                <MenuItem value={"bruftoinlandsprodukt_in_jeweiligen_preisen"}>Bruftoinlandsprodukt in jeweiligen
                    Preisen</MenuItem>
                <MenuItem value={"erwerbstaefige"}>Erwerbstäfige (Inlandskonzept)</MenuItem>
            </Select>
        </FormControl>
    );
}

export default TableDrop;
