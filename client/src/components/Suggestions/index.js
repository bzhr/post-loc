import * as React from "react";
import { Box, Flex } from "rebass";

const Suggestions = ({ data, setQuery, query, setLimit }) => {
  return (
    <Flex flexWrap="wrap" my={2}>
      {data.map((item) => (
        <Box my={1} mx={2} key={item.name} sx={{ cursor: "pointer" }}>
          {item.name.toLowerCase().includes(query) && (
            <Box
              onClick={() => {
                setQuery(item.name);
                setLimit(3);
              }}
            >
              {item.name}
            </Box>
          )}
          {item.postcode.toLowerCase().includes(query) && (
            <Box
              onClick={() => {
                setQuery(item.postcode);
                setLimit(3);
              }}
            >
              {item.postcode}
            </Box>
          )}
        </Box>
      ))}
    </Flex>
  );
};

export default Suggestions;
