import * as React from "react";
import InputLabel from "@mui/material/InputLabel";
import MenuItem from "@mui/material/MenuItem";
import FormControl from "@mui/material/FormControl";
import Select from "@mui/material/Select";

function LevelDrop({level, setLevel}) {
    const handleChange = (event) => {
        setLevel(event.target.value);
    };

    return (
        <FormControl fullWidth>
            <InputLabel id="demo-simple-select-label">Level</InputLabel>
            <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={level}
                label="DistrictLevel"
                onChange={handleChange}
            >
                <MenuItem value={1}>Auf Bundeslandebene</MenuItem>
                <MenuItem value={2}>Auf Regierungsbezirk</MenuItem>
                <MenuItem value={3}>Auf Kreisebene</MenuItem>
            </Select>
        </FormControl>
    );
}

export default LevelDrop;
