from cf import logger


def main():
    logger.trace("Hello, trace world!")
    logger.debug("Hello, debug world!")
    logger.info("Hello, info world!")
    logger.success("Hello, success world!")
    logger.warning("Hello, warning world!")
    logger.error("Hello, error world!")
    logger.critical("Hello, critical world!")


if __name__ == "__main__":
    main()
