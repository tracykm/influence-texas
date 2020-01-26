import React, { useEffect } from "react";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import styled from "styled-components";

export const TabWrapper = styled.div`
  button {
    border-bottom: solid !important;
    border-bottom-style: inset !important;
  }
`;

function TabPanel(props) {
  const { children, value, index, ...other } = props;

  return (
    <Typography
      component="div"
      role="tabpanel"
      hidden={value !== index}
      id={`simple-tabpanel-${index}`}
      aria-labelledby={`simple-tab-${index}`}
      {...other}
    >
      {value === index && <Box>{children}</Box>}
    </Typography>
  );
}

function a11yProps(index) {
  return {
    id: `simple-tab-${index}`,
    "aria-controls": `simple-tabpanel-${index}`
  };
}

export default function SimpleTabs({ tabs = [], startTabIdx = 0 }) {
  const [value, setValue] = React.useState(startTabIdx);

  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  useEffect(() => setValue(startTabIdx), [startTabIdx]);

  return (
    <TabWrapper>
      <div position="static" style={{ margin: "1em 0" }}>
        <Tabs
          variant="fullWidth"
          indicatorColor="primary"
          textColor="primary"
          value={value}
          onChange={handleChange}
          aria-label="simple tabs example"
        >
          {tabs.map((t, i) => (
            <Tab key={t.label} label={t.label} {...a11yProps(i)} />
          ))}
        </Tabs>
      </div>
      {tabs.map((t, i) => (
        <TabPanel key={i} value={value} index={i}>
          {t.content}
        </TabPanel>
      ))}
    </TabWrapper>
  );
}