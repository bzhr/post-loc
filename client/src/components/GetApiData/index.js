import * as React from "react";
import axios from "axios";

import { API_URL } from "../../constants";
import ContentBox from "../ContentBox";

const GetApiData = (props) => {
  const [query, setQuery] = React.useState("");
  const [data, setData] = React.useState([]);
  const [limit, setLimit] = React.useState(3);
  const [offset, setOffset] = React.useState(0);
  React.useEffect(() => {
    const lowerCaseQuery = query.toLowerCase();
    const fetchData = async () => {
      if (query.length >= 2) {
        const url = `${API_URL}?q=${lowerCaseQuery}&limit=${limit}&offset=${offset}`;
        console.log("Fetching data: ", url);
        const result = await axios(url);
        setData(data.length > 0 ? data.concat(result.data) : result.data);
      }
    };

    setTimeout(fetchData, 100);
  }, [query, limit, offset]);
  return (
    <ContentBox
      data={data}
      setQuery={setQuery}
      query={query}
      limit={limit}
      setLimit={setLimit}
      offset={offset}
      setOffset={setOffset}
    ></ContentBox>
  );
};
export default GetApiData;
