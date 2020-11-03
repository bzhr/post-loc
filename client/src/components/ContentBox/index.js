import * as React from "react";
import { Box, Flex } from "rebass";

import SearchBox from "../SearchBox";
import Suggestions from "../Suggestions";
import Results from "../Results";

const ContentBox = (props) => {
  return (
    <Box
      sx={{
        maxWidth: 600,
        mx: "auto",
      }}
      bg="lightgray"
      width={[1, 1, 1 / 2]}
    >
      <Flex flexDirection="column">
        <SearchBox {...props} />
        <Suggestions {...props} />
        <Results data={props.data} />
      </Flex>
    </Box>
  );
};

export default ContentBox;
