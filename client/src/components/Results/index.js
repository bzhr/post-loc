import * as React from "react";
import { Box, Flex, Text } from "rebass";
import { useScrollPosition } from "@huse/scroll-position";

const Results = ({ data, setOffset, limit, setLimit }) => {
  const ref = React.useRef(null);
  const position = useScrollPosition(ref.current);
  console.log(useScrollPosition);
  console.log("Position: ", position.y);
  if (position.y > 20) {
    setOffset(data.length);
    setLimit("");
  }
  return (
    <Flex my={3} flexDirection="column">
      <Text fontSize={[3, 4, 5]} fontWeight="bold" color="primary">
        Results
      </Text>
      <Flex
        ref={ref}
        height={75}
        sx={{ overflow: "auto" }}
        my={3}
        mx={6}
        flexDirection="column"
      >
        {data.map((item) => (
          <Flex my={2} key={item.name}>
            <Box width={1 / 2}>{item.name}</Box>
            <Box width={1 / 2}>{item.postcode}</Box>
          </Flex>
        ))}
      </Flex>
    </Flex>
  );
};

export default Results;
